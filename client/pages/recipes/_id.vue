<template>
  <v-container>
    <v-row md-4 xs-12>
      <v-col>
        <TweetCard :tweetLink="this.tweetLink" />
      </v-col>
    </v-row>
  </v-container>
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
