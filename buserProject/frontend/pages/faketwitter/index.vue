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
  //P
  asyncData() {
  	return AppApi.list_tweets().then(
  		(result) => { return {
  			tweets: result.data
  		}
  	})
  },
  data () {
    return {}
  },
  mounted() {
  	AppApi.list_tweets().then((result) => {
  		this.tweets = result.data;
  	});
  }
}
</script>

<style>
</style>
