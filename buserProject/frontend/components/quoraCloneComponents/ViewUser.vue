<template>
	<div>
		<usercard :user="user"></usercard>
		<timeline :questions="questions"></timeline>
	</div>
</template>

<script>

import timeline from '~/components/quoraCloneComponents/QuestionsTimeline.vue'
import usercard from '~/components/quoraCloneComponents/UserCard.vue' 

export default {
  layout: "quoraclone",
  props: ['user', 'questions'],
  components: {timeline, usercard},
  data () {
    return {
    }
  }
}
</script>

<style>
</style>
