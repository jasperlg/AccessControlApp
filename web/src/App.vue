<script setup lang="ts">
import SideMenu from "./components/SideMenu.vue";
</script>

<template>
<div class="dark w-screen h-screen relative dark:bg-gray-700 bg-gray-100 grid grid-cols-10 overflow-hidden">
  <div
    class="col-span-2 sm:col-span-4 lg:col-span-2 dark:bg-gray-700 bg-white h-full"
  >
    <SideMenu></SideMenu>
  </div>
</div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
