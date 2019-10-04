<template>
	<userslist :users="users"></userslist>
</template>

<script>

import userslist from '~/components/quoraCloneComponents/UsersList.vue' 
import AppApi from '~apijs'

export default {
  layout: "quoraclone",
  components: {
  	userslist
  },
  asyncData() {
  	return AppApi.users_list().then(
  		(result) => { return {
  			users: result.data
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