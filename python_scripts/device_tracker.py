triggered_entity = data.get('entity_id')
device_tracker_name = "device_tracker." + data.get('tracker_name')

current_state = hass.states.get(device_tracker_name)
new_state = hass.states.get(triggered_entity)

new_latitude = None
new_longitude = None
new_gps_accuracy = None
new_icon = None
new_battery = None
new_status = None

new_source_type = new_state.attributes.get('source_type')

if current_state is not None:
    new_latitude = current_state.attributes.get('latitude')
    new_longitude = current_state.attributes.get('longitude')
    new_gps_accuracy = current_state.attributes.get('gps_accuracy')
    new_icon = current_state.attributes.get('icon')
    new_battery = current_state.attributes.get('battery')
    new_status = current_state.state

if new_source_type == 'gps':
    new_latitude = new_state.attributes.get('latitude')
    new_longitude = new_state.attributes.get('longitude')
    new_gps_accuracy = new_state.attributes.get('gps_accuracy')

if new_state.attributes.get('battery') is not None:
    new_battery = new_state.attributes.get('battery')

if new_state.state == 'home':
    new_status = 'home'
    new_icon = 'mdi:home-map-marker'
elif new_state.state == 'not_home' and new_source_type == 'gps':
    new_status = 'not_home'
    new_icon = 'mdi:home'

hass.states.set(device_tracker_name, new_status, {
    'icon': new_icon,
    'friendly_name': data.get('tracker_name').capitalize(),
    'source_type': new_source_type,
    'battery': new_battery,
    'gps_accuracy': new_gps_accuracy,
    'latitude': new_latitude,
    'longitude': new_longitude,
    'last_update_source': new_state.name
})
