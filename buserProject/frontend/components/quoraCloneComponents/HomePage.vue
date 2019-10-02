<template>
  <timeline :questions="questions"></timeline>
</template>

<script>

import timeline from '~/components/quoraCloneComponents/QuestionsTimeline.vue' 

export default {
  layout: "quoraclone",
  props: ['questions'],
  components: {
  	 timeline
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
