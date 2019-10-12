import { Module, VuexModule, Mutation, Action } from 'vuex-module-decorators'
import algoliasearch from 'algoliasearch'
import config from '~/algolia.config.js'

const client = algoliasearch(config.appId, config.apiKey)
const index = client.initIndex('quasar_firestore')


@Module({ stateFactory: true, namespaced: true, name: 'search' })
export default class Search extends VuexModule {

    queryString: string = '';
    BuzzList: string[] = [];
    TweetObject: string[] = [];

    @Mutation
    public setBuzzList(resultBuzz: string[]) {
        this.BuzzList = resultBuzz;
    }

    @Mutation
    public setQueryString(queryString: string) {
        this.queryString = queryString;
    }

    @Mutation
    public setTweetObject(ObjectID: string[]) {
        this.TweetObject = ObjectID
        console.log(this.TweetObject)
    }

    // この2つ後でいい感じに共通化する
    @Action({ commit: 'setBuzzList' })
    public async query() {
        const searchResult = await index.search({ query: this.queryString })
        return searchResult.hits;
    }

    @Action({ commit: 'setTweetObject' })
    public async search() {
        const searchResult = await index.getObject(this.queryString)
        return searchResult
    }

}
