<template>
	<div>
    <questioncard :questionwrapper="questionwrapper" :answers="answers"></questioncard>
    <newanswer :questionwrapper="questionwrapper" @newanswer=addToAnswers($event.data)></newanswer>
  </div>
</template>

<script>

import questioncard from '~/components/quoraCloneComponents/QuestionCard.vue'
import newanswer from '~/components/quoraCloneComponents/NewAnswer.vue' 

export default {
  layout: "quoraclone",
  props: ['questionwrapper', 'answers'],
  components: {
    questioncard,
    newanswer
  },
  methods: {
    addToAnswers(answer) {
      this.answers.push(answer)
    }
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
