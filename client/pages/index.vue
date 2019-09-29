<template>
  <section class="container">
    <div>
      <v-text-field v-model="query" label="Regular" />
    </div>
    <v-layout row wrap>
      <v-flex v-for="todo in todoList" :key="todo.objectID" xs12 md4>
        <v-card class="grey ma-2">
          <blockquote class="twitter-tweet" data-dnt="true">
            <a :href="todo.tweetLink" />
          </blockquote>
          <script
            async
            src="https://platform.twitter.com/widgets.js"
            charset="utf-8"
          ></script>
        </v-card>
      </v-flex>
    </v-layout>
  </section>
</template>

<script lang="ts">
import * as algoliasearch from 'algoliasearch'
import config from '~/algolia.config.js'

const client = algoliasearch(config.appId, config.apiKey)
const index = client.initIndex('quasar_firestore')

export default {
  data() {
    return {
      todoInput: {
        title: '',
        description: '',
        done: false
      },
      registerModalIsVisible: false,
      query: '',
      todoList: []
    }
  },
  watch: {
    async query() {
      const searchResult = await index.search({ query: this.query })
      this.todoList = searchResult.hits
    }
  },
  async asyncData() {
    const searchResult = await index.search({ query: '' })
    return {
      todoList: searchResult.hits
    }
  }
}
</script>
