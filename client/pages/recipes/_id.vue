<template>
  <div>
    <v-card class="d-flex flex-row" flat tile>
      <TweetCard :tweetLink="this.tweetLink" />
      <v-card class="flex-grow-1">
        <v-card-title>材料</v-card-title>
        <v-card-text>
          <div>･なす</div>
          <div>･バター</div>
        </v-card-text>
      </v-card>
    </v-card>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { searchStore } from '~/store'

@Component({
  components: {
    TweetCard: () => import('@/components/TweetCard.vue')
  }
})
export default class Detail extends Vue {
  objectId: string = ''

  mounted(): void {
    this.objectId = this.$nuxt.$route.params.id
    console.log(this.objectId)
    searchStore.setQueryString(this.objectId)
    searchStore.search()
  }
  get tweetLink(): string {
    return searchStore.TweetObject.tweetLink
  }
}
</script>
