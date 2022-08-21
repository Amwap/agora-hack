<template>
  <div>
    <!-- <Header/> -->
    <RouterView />
  </div>
</template>

<script setup>
import Header from "@/components/Header.vue";
import { RouterLink, RouterView } from "vue-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
</script>

<style style="scss">
</style>
