<template>
    <div class="scrollbar-container">
        <div class="content" id="custom-scrollbars-content" ref="contentRef">
            <slot></slot>
        </div>
        <div class="scrollbar">
            <button class="button button--up" @click="handleScrollButton('up')">
                ↑
            </button>
            <div
                class="track-and-thumb"
                role="scrollbar"
                aria-controls="custom-scrollbars-content"
            >
                <div
                    class="track"
                    ref="scrollTrackRef"
                    @click="handleTrackClick"
                    :style="{ cursor: isDragging ? 'grabbing' : undefined }"
                ></div>
                <div
                    class="thumb"
                    ref="scrollThumbRef"
                    @mousedown="handleThumbMousedown"
                    :style="{
                        height: thumbHeight + 'px',
                        cursor: isDragging ? 'grabbing' : 'grab',
                    }"
                ></div>
            </div>
            <button
                class="button button--down"
                @click="handleScrollButton('down')"
            >
                ↓
            </button>
        </div>
    </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';

export default {
  name: 'Scrollbar',
  props: {
    children: {
      type: Array,
      default: () => [],
    },
  },
  setup() {
    const contentRef = ref(null);
    const scrollTrackRef = ref(null);
    const scrollThumbRef = ref(null);
    const observer = ref(null);

    const thumbHeight = ref(20);
    const isDragging = ref(false);
    const scrollStartPosition = ref(0);
    const initialContentScrollTop = ref(0);

    function handleResize() {
      if (scrollTrackRef.value && contentRef.value) {
        const { clientHeight: trackSize } = scrollTrackRef.value;
        const { clientHeight: contentVisible, scrollHeight: contentTotalHeight } =
          contentRef.value;
        thumbHeight.value = Math.max(
          (contentVisible / contentTotalHeight) * trackSize,
          20
        );
      }
    }

    function handleThumbPosition() {
      if (
        !contentRef.value ||
        !scrollTrackRef.value ||
        !scrollThumbRef.value
      ) {
        return;
      }

      const { scrollTop: contentTop, scrollHeight: contentHeight } =
        contentRef.value;
      const { clientHeight: trackHeight } = scrollTrackRef.value;

      let newTop = (contentTop / contentHeight) * trackHeight;
      newTop = Math.min(newTop, trackHeight - thumbHeight.value);

      const thumb = scrollThumbRef.value;
      requestAnimationFrame(() => {
        thumb.style.top = `${newTop}px`;
      });
    }

    onMounted(() => {
      if (contentRef.value) {
        const content = contentRef.value;
        observer.value = new ResizeObserver(() => {
          handleResize();
        });
        observer.value.observe(content);
        content.addEventListener('scroll', handleThumbPosition);
      }
    });

    onBeforeUnmount(() => {
      if (contentRef.value) {
        observer.value?.unobserve(contentRef.value);
        contentRef.value.removeEventListener('scroll', handleThumbPosition);
      }
    });

    function handleThumbMousedown(e) {
      e.preventDefault();
      e.stopPropagation();
      scrollStartPosition.value = e.clientY;
      if (contentRef.value) {
        initialContentScrollTop.value = contentRef.value.scrollTop;
      }
      isDragging.value = true;
    }

    function handleThumbMouseup(e) {
      e.preventDefault();
      e.stopPropagation();
      if (isDragging.value) {
        isDragging.value = false;
      }
    }

    function handleThumbMousemove(e) {
      if (contentRef.value) {
        e.preventDefault();
        e.stopPropagation();
        if (isDragging.value) {
          const {
            scrollHeight: contentScrollHeight,
            clientHeight: contentClientHeight,
          } = contentRef.value;

          const deltaY =
            (e.clientY - scrollStartPosition.value) *
            (contentClientHeight / thumbHeight.value);

          const newScrollTop = Math.min(
            initialContentScrollTop.value + deltaY,
            contentScrollHeight - contentClientHeight
          );

          contentRef.value.scrollTop = newScrollTop;
        }
      }
    }


onMounted(() => {
      document.addEventListener('mousemove', handleThumbMousemove);
      document.addEventListener('mouseup', handleThumbMouseup);
    });

    onBeforeUnmount(() => {
      document.removeEventListener('mousemove', handleThumbMousemove);
      document.removeEventListener('mouseup', handleThumbMouseup);
    });

    function handleTrackClick(e) {
      e.preventDefault();
      e.stopPropagation();
      const track = scrollTrackRef.value;
      const content = contentRef.value;
      if (track && content) {
        const { clientY } = e;
        const rect = track.getBoundingClientRect();
        const trackTop = rect.top;
        const thumbOffset = -(thumbHeight.value / 2);
        const clickRatio =
          (clientY - trackTop + thumbOffset) / track.clientHeight;
        const scrollAmount = Math.floor(clickRatio * content.scrollHeight);
        content.scrollTo({
          top: scrollAmount,
          behavior: 'smooth',
        });
      }
    }

    function handleScrollButton(direction) {
      const content = contentRef.value;
      if (content) {
        const scrollAmount = direction === 'down' ? 200 : -200;
        content.scrollBy({ top: scrollAmount, behavior: 'smooth' });
      }
    }

    return {
      contentRef,
      scrollTrackRef,
      scrollThumbRef,
      thumbHeight,
      isDragging,
      handleThumbMousedown,
      handleTrackClick,
      handleScrollButton,
    };
  },
};
</script>

<style scoped>
    .scrollbar-container {
        display: grid;
        height: 100%;
        grid-template: auto / 1fr 50px;
        overflow: hidden;
        position: relative;
    }

    .content {
        -ms-overflow-style: none;
        overflow: auto;
        scrollbar-width: none;
        height: 80vh;
    }

    .content::-webkit-scrollbar {
        display: none;
    }

    .scrollbar {
        display: grid;
        gap: 1rem;
        grid-auto-flow: row;
        grid-template: auto 1fr auto / 1fr;
        padding: 1rem;
        place-items: center;
    }

    .track-and-thumb {
        display: block;
        height: 100%;
        position: relative;
        width: 16px;
    }

    .track {
        bottom: 0;
        cursor: pointer;
        position: absolute;
        top: 0;
        border-radius: 12px;
        width: 16px;
        background: #fb923c;
    }

    .thumb {
        position: absolute;
        border-radius: 12px;
        background-color: #ff7300;
        /* mix-blend-mode: overlay; */
        width: 16px;
    }

    .button {
        border: none;
        border-radius: 50%;
        color: #fb923c;
        cursor: pointer;
    }

    .button--up {
        background: none;
    }

    .button--down {
        background: none;
    }
</style>
