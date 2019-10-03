<template>
<div>
  <newquestion @newquestion=addToTimeline($event.data)></newquestion>
  <timeline :questions="questions"></timeline>
</div>
</template>

<script>

import timeline from '~/components/quoraCloneComponents/QuestionsTimeline.vue'
import newquestion from '~/components/quoraCloneComponents/NewQuestion.vue' 

export default {
  layout: "quoraclone",
  props: ['questions'],
  components: {
  	 timeline,
  	 newquestion
  },
  methods: {
  	addToTimeline(question) {
  		this.questions.push(question)
  	}
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
