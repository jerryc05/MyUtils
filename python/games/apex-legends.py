#!/usr/bin/env python3

shadow_ok_ = ''
while shadow_ok_.lower() not in ('y', 'n'):
    shadow_ok_ = input('Enable shadow [Y/n]? ')
shadow_ok = shadow_ok_.lower() == 'y'

nv_gpu_ = ''
while nv_gpu_.lower() not in ('y', 'n'):
    nv_gpu_ = input('Using Nvidia GPU [Y/n]? ')
nv_gpu = nv_gpu_.lower() == 'y'

# videoconfig.txt
# Config:
"setting.cl_ragdoll_*" "0"
"setting.mat_depthfeather_enable" "0"
"setting.r_lod_switch_scale" "0.35"
"setting.csm_*" "0"  # shadows

# Autoexec:
(f'''
bind "F1" "toggle net_netGraph2 1 0; cl_showpos 1 0"    // Toggle for the FPS Counter
bind "F2" "toggle shownet_enabled 1 0"                  // Net Graph Toggle
bind "MWHEELDOWN" "+jump" 0     // Bhop
bind "MWHEELUP"   "+jump" 0     // Bhop
bind_US_standard "f"      "+ping"        0              // Ping (tap or hold)
bind_US_standard "mouse3" "ping_specific_type ENEMY" 0  // Ping enemy
bind_US_standard "mouse4" "+offhand1"    0              // Tactical ability
bind_US_standard "mouse5" "+melee"       0              // Quick melee attack
bind_US_standard "q"      "+weaponcycle" 0              // Cycle weapon
chroma_enable 0                 // Disables Razer Chroma
cl_forcepreload 1
cl_fovScale "1.6"               // 1.55 = 110FOV | 1.7 = 120FOV
cl_ragdoll_collide 0
cl_showfps "4"
fps_max "200"
hud_setting_minimapRotate "1"   // This setting allows the minimap to rotate with you (default 0)
hud_setting_pingAlpha "0.4"     // Opacity of the pings and downed banners (default 1)
m_acceleration "0"              // Once again this makes sure mouse acceleration is off
m_filter "0"                    // Makes sure any kind of mouse filtering is off
m_rawinput "1"                  // Takes the direct input of your mouse
mat_bloom_scalefactor_scalar 0  // Disables bloom (nothing to do with recoil, just the graphical effect you fn weirdo)
mat_compressedtextures 1
mat_screen_blur_enabled 0
mouse_sensitivity "1.3"         // Your mouse sensitivity
noise_filter_scale 0            // Removes Film-grain
player_setting_damage_closes_deathbox_menu "0"          // Your inventory wont auto-close anymore when receiving damage
r_dxgi_max_frame_latency 0
r_dynamic 0
r_fastzreject "{-1 if nv_gpu else 0}"
r_fullscreen 1
r_particle_timescale 3
sprint_view_shake_style "1"     // Less Headbob
telemetry_client_enable 0
telemetry_client_sendInterval 0
twitch_prime_linked 1
{"r_shadows 0" if shadow_ok else ""}
''')
