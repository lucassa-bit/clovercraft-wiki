import * as THREE from 'three'

type Appearance = { parts: string[]; forms: Record<string, string[]> }

// GeckoLib files contain every transform and held prop in one geometry. The
// game renderer hides the unused bones at runtime; reproduce that portrait
// rule here so a wiki model represents one form rather than the whole rig.
const astaParts = ['horn_r1', 'horn_l1', 'horn_side_r', 'horn_side_l', 'du_crown', 'du_chest', 'demon_upper_r', 'demon_fore_r', 'demon_hand_r', 'demon_upper_l', 'demon_fore_l', 'demon_hand_l', 'du_shoulder_r', 'du_shoulder_l', 'du_thigh_r', 'du_thigh_l', 'du_shin_r', 'du_shin_l', 'wing_r_1', 'wing_l_1', 'tail_1']
const astaArm = ['demon_upper_r', 'demon_fore_r', 'demon_hand_r']
const yunoParts = ['bell', 'dive_arm_l', 'dive_fore_l', 'dive_hand_l', 'dive_arm_r', 'dive_fore_r', 'dive_hand_r', 'dive_crown_l', 'dive_crown_r', 'dive_wing_l', 'dive_wing_r', 'zephyr_mantle', 'grimoire_star', 'broom']
const diveLeft = ['dive_arm_l', 'dive_fore_l', 'dive_hand_l', 'dive_crown_l', 'dive_wing_l']
const noelleBase = ['wand_r', 'cape_collar', 'cape_back_1', 'cape_shoulder_r', 'cape_shoulder_l', 'blazer', 'sleeve_r', 'sleeve_l', 'tunic_tail_r', 'tunic_tail_l', 'belt', 'pouch']
const valkyrie = ['vd_tiara', 'vd_ear_wing_l', 'vd_ear_wing_r', 'vd_breastplate', 'vd_faulds', 'vd_spaulder_l', 'vd_spaulder_r', 'vd_vambrace_l', 'vd_vambrace_r', 'vd_greave_l', 'vd_greave_r', 'vd_back_wing_l', 'vd_back_wing_r', 'vd_lance']
const saint = [...valkyrie.filter((bone) => !['vd_tiara', 'vd_back_wing_l', 'vd_back_wing_r', 'vd_lance'].includes(bone)), 'sv_crown', 'sv_halo', 'sv_wing_l', 'sv_wing_r', 'sv_lance']
const mereRobe = ['cape_collar', 'scarf', 'cape_long', 'cape_long_2', 'cape_shoulder_r', 'cape_shoulder_l', 'coat_f', 'coat_b', 'coat_side_r', 'coat_side_l']
const mereClothes = ['coat', 'sash', 'sleeve_r', 'sleeve_l', 'pants_r', 'pants_l', 'pants_shin_r', 'pants_shin_l', 'boot_r', 'boot_l', 'mane']
const hellfire = ['hf_streamer_r', 'hf_streamer_l', 'hf_crown', 'hf_skirt', 'hf_wrist_r', 'hf_wrist_l', 'hf_ankle_r', 'hf_ankle_l']
const leonum = ['lm_crown', 'lm_collar', 'lm_skirt', 'lm_foot_r', 'lm_foot_l', 'lm_wrist_r', 'lm_wrist_l']

const APPEARANCES: Record<string, Appearance> = {
  asta: {
    parts: astaParts,
    forms: {
      base: [], ba1: astaArm, ba2: [...astaArm, 'horn_r1', 'wing_r_1'],
      ba3: [...astaArm, 'demon_fore_l', 'demon_hand_l', 'horn_r1', 'horn_l1', 'wing_r_1'],
      du: [...astaArm, 'demon_upper_l', 'demon_fore_l', 'demon_hand_l', 'horn_side_r', 'horn_side_l', 'du_crown', 'du_chest', 'du_shoulder_r', 'du_shoulder_l', 'du_thigh_r', 'du_thigh_l', 'du_shin_r', 'du_shin_l', 'wing_r_1', 'wing_l_1', 'tail_1'],
    },
  },
  yuno: {
    parts: yunoParts,
    forms: {
      base: [], dive: diveLeft,
      zephyr: [...diveLeft, 'dive_arm_r', 'dive_fore_r', 'dive_hand_r', 'dive_crown_r', 'dive_wing_r', 'zephyr_mantle', 'grimoire_star'],
    },
  },
  noelle: { parts: [...noelleBase, ...valkyrie, ...saint], forms: { base: noelleBase, valkyrie, saint } },
  mereoleona: { parts: [...mereRobe, ...mereClothes, ...hellfire, ...leonum], forms: { base: [...mereRobe, ...mereClothes], hellfire: [...mereClothes, ...hellfire], hellfire2: [...mereClothes, ...hellfire], hellfire3: [...mereClothes, ...hellfire], leonum } },
}

const HELD_PROPS = new Set(['grimoire', 'grimoire_cover', 'grimoire_page', 'grimoire_page2', 'grimoire_page3', 'divider_r', 'divider_l', 'sword_surf'])

export function applyCharacterAppearance(root: THREE.Object3D, character: string, form: string): void {
  const rule = APPEARANCES[character]
  const hidden = new Set<string>(HELD_PROPS)
  root.traverse((object) => { object.visible = true })
  root.traverse((object) => {
    if (object.name.startsWith('sword_') || object.name === 'wand_r') hidden.add(object.name)
  })
  if (rule) {
    for (const part of rule.parts) hidden.add(part)
    for (const part of rule.forms[form] ?? rule.forms.base ?? []) hidden.delete(part)
  }
  root.traverse((object) => { if (hidden.has(object.name)) object.visible = false })
}
