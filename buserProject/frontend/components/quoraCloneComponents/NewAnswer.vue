<template>
<div>
  <v-btn color="blue" block v-if="logged_user" @click="goanswer()">New Answer</v-btn>
  <textarea-dialog ref="newanswerdialog"></textarea-dialog>
</div>
</template>

<script>

import textareaDialog from '~/components/TextAreaDialog.vue'
import AppApi from '~apijs'

export default {
  layout: "quoraclone",
  props: ['questionwrapper'],
  components: {
    textareaDialog
  },
  computed: {
    logged_user() {
      return this.$store.getters.logged_user
    }
  },
  data () {
    return {}
  },
  methods: {
    goanswer () {
      this.$refs.newanswerdialog.open({
        title: "New Answer",
        label: "Type the answer",
        value: '',
        action: 'Post Answer',
        actionFunc: value => {
          return AppApi.post_answer(this.questionwrapper.question.title, this.questionwrapper.question.author_username, value).then(answer => {
            this.$emit('newanswer', answer)});
        }
      })
    }
  }
}
</script>

<style>
</style>