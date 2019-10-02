<template>
  <timeline :tweets="tweets"></timeline>
</template>

<script>

import timeline from '~/components/fakeTwitterComponents/Timeline.vue' 

export default {
  layout: "faketwitter",
  props: ['tweets'],
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
