import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Clover Craft Wiki',
  description: 'Wiki do mod Clover Craft 0.4.0 (NeoForge 1.21.1)',
  lang: 'pt-BR',
  base: process.env.VITEPRESS_BASE || '/',
  cleanUrls: true,
  lastUpdated: true,
  vite: {
    ssr: {
      noExternal: ['three'],
    },
  },
  themeConfig: {
    logo: '/clover.svg',
    outline: 'deep',
    search: { provider: 'local' },
    nav: [
      { text: 'Guia', link: '/guia/comecar' },
      { text: 'Personagens', link: '/personagens/' },
      { text: 'Galeria 3D', link: '/galeria' },
      { text: 'Mundo', link: '/mundo/' },
      { text: 'Sistemas', link: '/sistemas/squads' },
      { text: 'Sobre', link: '/sobre' },
    ],
    sidebar: {
      '/guia/': [
        {
          text: 'Guia',
          items: [
            { text: 'Começar', link: '/guia/comecar' },
            { text: 'Controles', link: '/guia/controles' },
            { text: 'Combate', link: '/guia/combate' },
            { text: 'Progressão', link: '/guia/progressao' },
          ],
        },
      ],
      '/personagens/': [
        {
          text: 'Personagens',
          items: [
            { text: 'Visão geral', link: '/personagens/' },
            { text: "Asta", link: "/personagens/asta" },
              { text: "Yuno", link: "/personagens/yuno" },
              { text: "Yami Sukehiro", link: "/personagens/yami" },
              { text: "Noelle Silva", link: "/personagens/noelle" },
              { text: "Mereoleona Vermillion", link: "/personagens/mereoleona" },
              { text: "Julius Novachrono", link: "/personagens/julius" },
              { text: "Nacht Faust", link: "/personagens/nacht" },
              { text: "Licht", link: "/personagens/licht" },
              { text: "Dante Zogratis", link: "/personagens/dante" },
              { text: "Luck Voltia", link: "/personagens/luck" },
              { text: "Mimosa Vermillion", link: "/personagens/mimosa" },
              { text: "Vanica Zogratis", link: "/personagens/vanica" },
              { text: "Zenon Zogratis", link: "/personagens/zenon" },
              { text: "Zora Ideale", link: "/personagens/zora" },
              { text: "Vanessa Enoteca", link: "/personagens/vanessa" },
              { text: "Gauche Adlai", link: "/personagens/gauche" },
          ],
        },
      ],
      '/mundo/': [
        {
          text: 'Mundo',
          items: [
            { text: 'Overworld', link: '/mundo/' },
            { text: 'Chefes', link: '/mundo/bosses' },
            { text: 'Submundo', link: '/mundo/underworld' },
          ],
        },
      ],
      '/sistemas/': [
        {
          text: 'Sistemas',
          items: [
            { text: 'Esquadrões', link: '/sistemas/squads' },
            { text: 'Guildas', link: '/sistemas/guildas' },
            { text: 'Raças', link: '/sistemas/racas' },
            { text: 'Árvore', link: '/sistemas/arvore' },
            { text: 'Quests', link: '/sistemas/quests' },
            { text: 'Invocações', link: '/sistemas/invocacoes' },
            { text: 'Relíquias', link: '/sistemas/reliquias' },
            { text: 'Itens', link: '/sistemas/itens' },
            { text: 'Comandos', link: '/sistemas/comandos' },
          ],
        },
      ],
    },
    socialLinks: [],
    footer: {
      message: 'Fan wiki gerada a partir do JAR 0.4.0. Black Clover pertence a Yūki Tabata / Shueisha.',
      copyright: 'Clover Craft 0.4.0 · NeoForge 1.21.1',
    },
  },
  head: [
    ['link', { rel: 'icon', href: '/clover.svg' }],
  ],
})
