#include "ui.h"

int main()
{
    uiControlShow(uiControl(uiNewWindow("libui test", 320, 240, 1)));
    uiMain();
    uiUninit();
}
