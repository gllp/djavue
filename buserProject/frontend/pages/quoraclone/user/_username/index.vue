<template>
  <viewuser :user="user" :questions="questions"></viewuser>
</template>

<script>

import viewuser from '~/components/quoraCloneComponents/ViewUser.vue'
import AppApi from '~apijs'

export default {
  components: {
    viewuser
  },
  layout: "quoraclone",
  asyncData(context) {
    const username = context.params.username
    return Promise.all([AppApi.list_questions(username), AppApi.get_user_details(username)]).then(results => {
        return {
          questions: results[0].data,
          user: results[1].data
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
