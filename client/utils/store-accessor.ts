import { Store } from 'vuex'
import { getModule } from 'vuex-module-decorators'
import Search from '~/store/search'

let searchStore: Search

function initialiseStores(store: Store<any>): void {
  searchStore = getModule(Search, store)
}

export { initialiseStores, searchStore }