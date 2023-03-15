APP_DIR := app
TARGET := $(MAKECMDGOALS)

include $(APP_DIR)/Makefile

.PHONY: $(TARGET)
$(TARGET):
	cd $(APP_DIR) && $(MAKE) $(TARGET)
	@true