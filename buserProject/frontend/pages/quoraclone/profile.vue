<template>
  <viewprofile :userprofile="userprofile"></viewprofile>
</template>

<script>

import viewprofile from '~/components/quoraCloneComponents/ViewProfile.vue'
import AppApi from '~apijs'

export default {
  components: {
    viewprofile
  },
  layout: "quoraclone",
  props: ['username'],
  asyncData(context) {
    const username = context.params.username
    return AppApi.get_profile(this.username).then(result => {
        return {
          userprofile: result.data
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
