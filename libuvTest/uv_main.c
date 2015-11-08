#include<stdio.h>
#include<stdlib.h>
#include<uv.h>

int64_t counter = 0;
void wait_for_a_while(uv_idle_t *handle) {
  counter++;
  printf("%lld\n", counter);
  if (counter >= 100)
    uv_idle_stop(handle);
}
int main(int argv, char *args[]) {
  uv_idle_t idle;
  uv_idle_init(uv_default_loop(), &idle);
  uv_idle_start(&idle, wait_for_a_while);

  printf("idle......\n");
  uv_run(uv_default_loop(), UV_RUN_DEFAULT);
  
  uv_loop_close(uv_default_loop());
  return 0;
}
