<script>
import moment from "moment";
export default {
  name: "TweetsTable",
  props: ["tweets"],
  methods: {
    moment,
  },
};
</script>
<template>
  <table class="table table-striped table-bordered">
    <thead>
      <th>Time</th>
      <th>Tweet</th>
      <th>Name</th>
    </thead>
    <tbody>
      <tr v-for="tweet in tweets" :key="tweet.id">
        <td>
          {{ moment(tweet.datetime, true).format("MMMM Do YYYY, h:mm:ss a") }}
        </td>
        <td>{{ tweet.tweet }}</td>
        <td>{{ tweet.name }}</td>
      </tr>
    </tbody>
  </table>
</template>
