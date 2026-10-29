import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import GeoViewer from './GeoViewer.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('GeoViewer', GeoViewer)
  },
} satisfies Theme
