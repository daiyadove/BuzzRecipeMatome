<template>
  <v-card class="grey ma-2">
    <blockquote class="twitter-tweet" data-dnt="true">
      <a :href="tweetLink" />
    </blockquote>
    <script
      async
      src="https://platform.twitter.com/widgets.js"
      charset="utf-8"
    ></script>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'

@Component
export default class DispTweet extends Vue {
  @Prop({ required: true }) tweetLink: String
}
</script>
