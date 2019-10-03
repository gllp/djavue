<template>
	<viewquestion :question="question" :answers="answers"></viewquestion>
</template>

<script>

import viewquestion from '~/components/quoraCloneComponents/ViewQuestion.vue'
import AppApi from '~apijs'

export default {
  components: {
    viewquestion
  },
  layout: "quoraclone",
  asyncData(context) {
  	const questiontitle = context.params.questiontitle
    const username = context.params.username
    return Promise.all([AppApi.get_question(questiontitle, username), AppApi.get_answers(questiontitle, username)]).then(results => {
      return {
        question: results[0].data,
        answers: results[1].data
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
