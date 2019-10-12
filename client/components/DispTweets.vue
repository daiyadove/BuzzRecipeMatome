<template>
  <v-layout row wrap>
    <v-flex v-for="tweet in BuzzList" :key="tweet.objectID" xs12 md4>
      <n-link
        :to="{
          name: 'recipes-id',
          params: { id: tweet.objectID }
        }"
      >
        <TweetCard :tweetLink="tweet.tweetLink" />
      </n-link>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { searchStore } from '~/store'

@Component({
  components: {
    TweetCard: () => import('../components/TweetCard.vue')
  }
})
export default class DispTweet extends Vue {
  get BuzzList(): string[] {
    return searchStore.BuzzList
  }
  public hoge() {
    console.log('ck')
  }
}
</script>
