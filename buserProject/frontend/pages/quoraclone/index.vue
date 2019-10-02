<template>
	<home :questions="questions"></home>
</template>

<script>

import home from '~/components/quoraCloneComponents/HomePage.vue' 
import AppApi from '~apijs'

export default {
  layout: "quoraclone",
  components: {
  	home
  },
  asyncData() {
  	return AppApi.list_questions().then(
  		(result) => { return {
  			questions: result.data
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