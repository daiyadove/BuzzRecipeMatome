<template>
  <section class="container">
    <div>
      <v-text-field v-model="queryString" label="検索" />
    </div>
    <DispTweets />
  </section>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator'
import { searchStore } from '~/store'

@Component({
  components: {
    DispTweets: () => import('../components/DispTweets.vue')
  }
})
export default class Search extends Vue {
  mounted(): void {
    searchStore.query()
  }
  @Watch('queryString')
  query() {
    searchStore.query()
  }
  get queryString(): string {
    return searchStore.queryString
  }
  set queryString(value: string) {
    searchStore.setQueryString(value)
  }
}
</script>
