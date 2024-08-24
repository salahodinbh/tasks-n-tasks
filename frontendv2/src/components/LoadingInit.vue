<template>
    <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-white z-50">
        <div class="animate-spin rounded-full h-32 w-32 border-t-4 border-blue-500 border-solid"></div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            visible: true,
        };
    },
    mounted() {
        setTimeout(() => {
            this.visible = false;
        }, 2000); // Duration of the loader
    }
}
</script>
