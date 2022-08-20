<template lang="">
    <div 
        class="p-1 item" 
        :class="`col-md-${item.width}`"
        v-for="item in canvas.item_list"
        > 
    </div>
</template>
<script>

export default {
    
}
</script>
<style lang="">
    
</style>