<template>
  <div>
    <TweetCard :tweetLink="this.tweetLink" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component({
  components: {
    TweetCard: () => import('@/components/TweetCard.vue')
  }
})
export default class DispTweet extends Vue {
  tweetLink: string = ''

  mounted(): void {
    this.tweetLink = this.$nuxt.$route.params.id
  }
}
</script>
