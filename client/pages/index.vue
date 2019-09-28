<template>
  <section class="container">
    <div>
      <logo />
      <h1 class="title">test</h1>
      <h2 class="subtitle">My awesome Nuxt.js project</h2>
      <div class="links">
        <a href="https://nuxtjs.org/" target="_blank" class="button--green"
          >Documentation</a
        >
        <a
          href="https://github.com/nuxt/nuxt.js"
          target="_blank"
          class="button--grey"
          >GitHub</a
        >
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component({
  components: {
    Logo: () => import('~/components/Logo.vue')
  }
})
export default class Index extends Vue {}
</script>
