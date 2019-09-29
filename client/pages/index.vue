<template>
  <section class="container">
    <div>
      <v-text-field v-model="query" label="Regular" />
    </div>
    <v-layout row wrap>
      <v-flex v-for="todo in todoList" :key="todo.objectID" xs4>
        <v-card class="grey ma-2">
          <blockquote class="twitter-tweet" data-dnt="true">
            <p lang="ja" dir="ltr">
              もはや焼き鳥のつくね串なしバージョン..
              <br />
              <br />袋で混ぜて簡単！<br />【レンジでジューシーつくね】<br /><br />袋に鶏ひき肉300g、片栗粉大さじ1、マヨ大さじ1、醤油大さじ1/2混ぜ容器に入れて
              4分チン。醤油小さじ2、みりん大さじ1、片栗粉小さじ1混ぜてかけ1分チンで完成<br /><br />レシピは動画からサイトへGO▼<a
                href="https://twitter.com/hashtag/%E3%81%97%E3%81%8B%E3%81%AA%E3%81%84%E6%96%99%E7%90%86?src=hash&amp;ref_src=twsrc%5Etfw"
                >#しかない料理</a
              >
              <a href="https://t.co/1WuZF7uzSd">pic.twitter.com/1WuZF7uzSd</a>
            </p>
            &mdash; #しかない料理のイガゴー＠究極の節約レシピ (@gogoigarashi)
            <a
              href="https://twitter.com/gogoigarashi/status/1176453725499490305?ref_src=twsrc%5Etfw"
              >September 24, 2019</a
            >
          </blockquote>
          <script
            async
            src="https://platform.twitter.com/widgets.js"
            charset="utf-8"
          ></script>
          <v-card-text>{{ todo.tweetID }}</v-card-text>
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
