import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import GeoViewer from './GeoViewer.vue'
import CharacterRoster from './CharacterRoster.vue'
import CharacterProfile from './CharacterProfile.vue'
import CharacterDetails from './CharacterDetails.vue'
import SystemsHub from './SystemsHub.vue'
import BossRoster from './BossRoster.vue'
import './custom.css'
import './characters.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('GeoViewer', GeoViewer)
    app.component('CharacterRoster', CharacterRoster)
    app.component('CharacterProfile', CharacterProfile)
    app.component('CharacterDetails', CharacterDetails)
    app.component('SystemsHub', SystemsHub)
    app.component('BossRoster', BossRoster)
  },
} satisfies Theme
