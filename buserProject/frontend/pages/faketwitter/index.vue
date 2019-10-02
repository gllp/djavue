<template>
  <home :tweets="tweets"></home>
</template>

<script>

import home from '~/components/fakeTwitterComponents/Home.vue' 
import AppApi from '~apijs'

export default {
  layout: "faketwitter",
  components: {
  	 home
  },
  //Used for top-level nuxt pages to return async data from promise requests.
  //Solves the SEO problem on site search.
  //The code can be executed both in the backend and in the browser.
  asyncData() {
  	return AppApi.list_tweets().then(
  		(result) => { return {
  			tweets: result.data
  		}
  	})
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
