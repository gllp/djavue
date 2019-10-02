<template>
	<h1>Timeline do usuario {{username}}</h1>
</template>

<script>

export default {
  layout: "faketwitter",
  asyncData(context) {
  	return {
  		username: context.params.username
  	}
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
