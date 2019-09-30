<template>
  <v-layout row wrap>
    <v-flex v-for="tweet in BuzzList" :key="tweet.objectID" xs12 md4>
      <v-card class="grey ma-2">
        <blockquote class="twitter-tweet" data-dnt="true">
          <a :href="tweet.tweetLink" />
        </blockquote>
        <script
          async
          src="https://platform.twitter.com/widgets.js"
          charset="utf-8"
        ></script>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { searchStore } from '~/store'

@Component
export default class Search extends Vue {
  get BuzzList(): string[] {
    return searchStore.BuzzList
  }
}
</script>
