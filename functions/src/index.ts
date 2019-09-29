import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin';
import DocumentSnapshot = FirebaseFirestore.DocumentSnapshot

admin.initializeApp()
const env = functions.config()

import * as algoliasearch from 'algoliasearch';

// Algolia Clientの初期化
const client = algoliasearch(env.algolia.appid, env.algolia.apikey);
// 作成したAlgoliaのIndex名を入れる
const index = client.initIndex('quasar_firestore');

// Recipeというコレクションにドキュメントが追加されたときに、
// algoliaにも、追加する設定
// exports.indexRecipe = functions.firestore
//   .document('recipe/{recipeId}')
//   .onWrite((change, context) => {
//     const data = .data();
//     const objectID = snap.id;

//     // Add the data to the algolia index
//     return index.addObject({
//       objectID,
//       ...data
//     });
// });
exports.indexRecipe = functions.firestore
  .document('recipe/{recipeId}')
  .onWrite((change: functions.Change<DocumentSnapshot>) => {
    const recipe = change.after.data()
    const objectID = change.after.id
    return index.saveObject(
        Object.assign({
          objectID,
          ...recipe
        })
    )
  });
