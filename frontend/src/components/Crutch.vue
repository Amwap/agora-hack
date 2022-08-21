<template lang="">
    <div class="preview" @click="$emin('hidePreview')">
        <div class="col-md-12 mt-3">
            <ItemTree
                class="m-auto"
                :item_list="canvas"
            />
        </div>
    </div>
    <button
        type="button"
        class="btn btn-block btn-warning btn-sm my-1"
        @click="$emin('hidePreview')"
    >
        Preview
    </button>
</template>
<script>
export default {
    props:{
        canvas: Object
    }
}
</script>
<style lang="scss" scoped>
.preview{
    display: fixed;
    position: absolute;
    z-index: 100;
    width: 100%;
    height: 100%;
    background-color: antiquewhite;
    
}
    
</style>