import * as THREE from 'three'

interface FaceUv {
  uv: [number, number]
  uv_size: [number, number]
}

interface Cube {
  origin: [number, number, number]
  size: [number, number, number]
  pivot?: [number, number, number]
  rotation?: [number, number, number]
  inflate?: number
  mirror?: boolean
  uv?: [number, number] | Record<string, FaceUv>
}

interface Bone {
  name: string
  parent?: string
  pivot?: [number, number, number]
  rotation?: [number, number, number]
  cubes?: Cube[]
}

interface Geometry {
  description: {
    texture_width: number
    texture_height: number
  }
  bones: Bone[]
}

const DEG = Math.PI / 180
const FACE_ORDER = ['north', 'east', 'south', 'west', 'up', 'down'] as const

type FaceName = (typeof FACE_ORDER)[number]

/** Vértices CCW vistos de fora. Ordem: BL, BR, TR, TL. */
function faceCorners(
  face: FaceName,
  x0: number,
  y0: number,
  z0: number,
  x1: number,
  y1: number,
  z1: number,
): number[][] {
  switch (face) {
    case 'north':
      return [
        [x1, y0, z0],
        [x0, y0, z0],
        [x0, y1, z0],
        [x1, y1, z0],
      ]
    case 'south':
      return [
        [x0, y0, z1],
        [x1, y0, z1],
        [x1, y1, z1],
        [x0, y1, z1],
      ]
    case 'west':
      return [
        [x0, y0, z0],
        [x0, y0, z1],
        [x0, y1, z1],
        [x0, y1, z0],
      ]
    case 'east':
      return [
        [x1, y0, z1],
        [x1, y0, z0],
        [x1, y1, z0],
        [x1, y1, z1],
      ]
    case 'up':
      return [
        [x0, y1, z1],
        [x1, y1, z1],
        [x1, y1, z0],
        [x0, y1, z0],
      ]
    case 'down':
      return [
        [x0, y0, z0],
        [x1, y0, z0],
        [x1, y0, z1],
        [x0, y0, z1],
      ]
  }
}

function boxUv(face: FaceName, u: number, v: number, sx: number, sy: number, sz: number): FaceUv {
  switch (face) {
    case 'up':
      return { uv: [u + sz, v], uv_size: [sx, sz] }
    case 'down':
      return { uv: [u + sz + sx, v], uv_size: [sx, sz] }
    case 'west':
      return { uv: [u, v + sz], uv_size: [sz, sy] }
    case 'north':
      return { uv: [u + sz, v + sz], uv_size: [sx, sy] }
    case 'east':
      return { uv: [u + sz + sx, v + sz], uv_size: [sz, sy] }
    case 'south':
      return { uv: [u + sz + sx + sz, v + sz], uv_size: [sx, sy] }
  }
}

function pushQuad(
  pos: number[],
  nrm: number[],
  uv: number[],
  idx: number[],
  corners: number[][],
  normal: [number, number, number],
  u0: number,
  v0: number,
  u1: number,
  v1: number,
): void {
  const base = pos.length / 3
  for (const c of corners) {
    pos.push(c[0], c[1], c[2])
    nrm.push(normal[0], normal[1], normal[2])
  }
  uv.push(u0, v0, u1, v0, u1, v1, u0, v1)
  idx.push(base, base + 1, base + 2, base, base + 2, base + 3)
}

function cubeGeometry(cube: Cube, originOffset: [number, number, number], texW: number, texH: number): THREE.BufferGeometry {
  const inf = cube.inflate ?? 0
  const [ox, oy, oz] = cube.origin
  const [sx, sy, sz] = cube.size
  const x0 = ox - inf - originOffset[0]
  const y0 = oy - inf - originOffset[1]
  const z0 = oz - inf - originOffset[2]
  const x1 = x0 + sx + inf * 2
  const y1 = y0 + sy + inf * 2
  const z1 = z0 + sz + inf * 2

  const pos: number[] = []
  const nrm: number[] = []
  const uvs: number[] = []
  const idx: number[] = []

  const normals: Record<FaceName, [number, number, number]> = {
    north: [0, 0, -1],
    south: [0, 0, 1],
    west: [-1, 0, 0],
    east: [1, 0, 0],
    up: [0, 1, 0],
    down: [0, -1, 0],
  }

  for (const face of FACE_ORDER) {
    let fu: FaceUv | undefined
    if (Array.isArray(cube.uv)) {
      fu = boxUv(face, cube.uv[0], cube.uv[1], sx, sy, sz)
    } else if (cube.uv && face in cube.uv) {
      fu = cube.uv[face]
    }
    if (!fu) continue

    const [u, v] = fu.uv
    const [uw, vh] = fu.uv_size
    const u0 = u / texW
    const vTop = 1 - v / texH
    const u1 = (u + uw) / texW
    const vBot = 1 - (v + vh) / texH
    pushQuad(pos, nrm, uvs, idx, faceCorners(face, x0, y0, z0, x1, y1, z1), normals[face], u0, vBot, u1, vTop)
  }

  const geo = new THREE.BufferGeometry()
  geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3))
  geo.setAttribute('normal', new THREE.Float32BufferAttribute(nrm, 3))
  geo.setAttribute('uv', new THREE.Float32BufferAttribute(uvs, 2))
  geo.setIndex(idx)
  return geo
}

function euler(rot?: [number, number, number]): THREE.Euler {
  if (!rot) return new THREE.Euler(0, 0, 0, 'XYZ')
  return new THREE.Euler(rot[0] * DEG, rot[1] * DEG, rot[2] * DEG, 'XYZ')
}

export function loadBedrockGeo(json: { 'minecraft:geometry': Geometry[] }, material: THREE.Material): THREE.Group {
  const geom = json['minecraft:geometry'][0]
  const texW = geom.description.texture_width || 64
  const texH = geom.description.texture_height || 64
  const root = new THREE.Group()
  root.name = 'bedrock-root'
  const nodes = new Map<string, THREE.Group>()

  for (const bone of geom.bones) {
    const g = new THREE.Group()
    g.name = bone.name
    g.position.set(...(bone.pivot ?? [0, 0, 0]))
    g.rotation.copy(euler(bone.rotation))
    nodes.set(bone.name, g)
  }

  for (const bone of geom.bones) {
    const g = nodes.get(bone.name)!
    if (bone.parent && nodes.has(bone.parent)) {
      const parent = nodes.get(bone.parent)!
      parent.add(g)
      const pp = geom.bones.find((b) => b.name === bone.parent)?.pivot ?? [0, 0, 0]
      g.position.x -= pp[0]
      g.position.y -= pp[1]
      g.position.z -= pp[2]
    } else {
      root.add(g)
    }

    const pivot = bone.pivot ?? [0, 0, 0]
    for (const cube of bone.cubes ?? []) {
      if (cube.rotation && cube.pivot) {
        const holder = new THREE.Group()
        holder.position.set(cube.pivot[0] - pivot[0], cube.pivot[1] - pivot[1], cube.pivot[2] - pivot[2])
        holder.rotation.copy(euler(cube.rotation))
        const mesh = new THREE.Mesh(cubeGeometry(cube, cube.pivot, texW, texH), material)
        mesh.castShadow = false
        holder.add(mesh)
        g.add(holder)
      } else {
        const mesh = new THREE.Mesh(cubeGeometry(cube, pivot, texW, texH), material)
        g.add(mesh)
      }
    }
  }

  return root
}

export function applyMaterial(root: THREE.Object3D, material: THREE.Material): void {
  root.traverse((obj) => {
    if (obj instanceof THREE.Mesh) {
      obj.material = material
    }
  })
}

export function disposeObject(root: THREE.Object3D): void {
  root.traverse((obj) => {
    if (obj instanceof THREE.Mesh) {
      obj.geometry.dispose()
    }
  })
}
