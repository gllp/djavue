<template>
	<h1>Pagina da pergunta {{questionid}}</h1>
</template>

<script>

export default {
  layout: "quoraclone",
  asyncData(context) {
  	return {
  		questionid: context.params.questionid
  	}
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
