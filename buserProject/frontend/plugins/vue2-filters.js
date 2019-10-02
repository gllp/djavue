import Vue from 'vue'
import Vue2Filters from 'vue2-filters'
import moment from 'moment'
 
Vue.use(Vue2Filters)

Vue.filter('json', value => {
  if (!value) return
  return JSON.stringify(value, null, 2)
})

Vue.filter('timelapsed', value => {
  return moment(value).fromNow()
})