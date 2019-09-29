import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin';
admin.initializeApp()
const env = functions.config()

import * as algoliasearch from 'algoliasearch';

// Algolia Clientの初期化
const client = algoliasearch(env.algolia.appid, env.algolia.apikey);
// 作成したAlgoliaのIndex名を入れる
const index = client.initIndex('quasar_firestore');

// Cityというコレクションにドキュメントが追加されたときに、
// algoliaにも、追加される設定です。
exports.indexCity = functions.firestore
  .document('recipe/{recipeId}')
  .onCreate((snap, context) => {
    const data = snap.data();
    const objectID = snap.id;

    // Add the data to the algolia index
    return index.addObject({
      objectID,
      ...data
    });
});