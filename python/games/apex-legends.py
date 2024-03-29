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
bind "MWHEELDOWN"           "+jump;+forward"    0
bind "MWHEELUP"             "+jump"             0
bind_US_standard "SPACE"    "+jump"             0
bind_US_standard "f9"       "exec autoexec"
bind_US_standard "f2"       "bind_US_standard mouse2   \"+toggle_zoom\"" // Toggle ADS
bind_US_standard "f3"       "bind_US_standard mouse2          \"+zoom\"" // Hold ADS
bind_US_standard "f"        "+ping"             0           // Ping (tap or hold)
bind_US_standard "mouse3"   "ping_specific_type ENEMY"  0   // Ping enemy
bind_US_standard "mouse4"   "+melee"            0           // Quick melee attack
bind_US_standard "mouse5"   "+offhand1"         0           // Tactical ability
bind_US_standard "v"        "+pushtotalk"       0           // Push-to-talk
bind_US_standard "q"        "+weaponcycle"      0           // Cycle weapon
bind_US_standard "5"        "use_consumable SHIELD_LARGE"  0  // Quick-use medpack (shield battery)
bind_US_standard "6"        "use_consumable SHIELD_SMALL"  0  // Quick-use medpack (shield cell)
bind_US_standard "7"        "use_consumable HEALTH_LARGE"  0  // Quick-use medpack (med kit)
bind_US_standard "8"        "use_consumable HEALTH_SMALL"  0  // Quick-use medpack (syringe)


ai_expression_frametime  0             //Disable expressions
anim_3wayblend  0
bink_materials_enabled  0
bink_preload_videopanel_movies  0
building_cubemaps  1
chroma_enable 0                 // Disables Razer Chroma
cl_SetupAllBones  0 //Do not force every animation component of a model to be set up
cl_aggregate_particles  1
cl_allowAnimsToInterpolateBackward  0
cl_always_ragdoll_radius  0
cl_anim_detail_dist  1
cl_anim_face_dist  1
cl_bones_incremental_blend  1
cl_cull_weapon_fx  0 //Disables weapon FX
cl_decal_alwayswhite  1
cl_detaildist  0 //Distance at which detail props are no longer visible
cl_detailfade  0 //Distance across which detail props fade in
cl_disable_ragdolls  1
cl_drawshadowtexture  0
cl_ejectbrass  0 //Disables brass ejection
cl_forcepreload 1
cl_fovScale "1.5"               // 1.55 = 110FOV | 1.7 = 120FOV
cl_gib_allow  0
cl_idealpitchscale  0
cl_jiggle_bone_framerate_cutoff  0
cl_lagcompensation  1
cl_minimal_rtt_shadows  1
cl_muzzleflash_dlight_st  0
cl_new_impact_effects  0
cl_particle_fallback_base "-1"
cl_particle_fallback_multiplier "-1"
cl_particle_limiter_max_particle_count 10
cl_particle_limiter_max_system_count 10
cl_particle_limiter_min_kill_distance  1
cl_particle_max_count  0
cl_particle_snoozetime "0.166667"
cl_phys_maxticks  0
cl_phys_props_enable  0 //Disable client side physics props
cl_predict  1 //Perform client side prediction.
cl_predictweapons  1 //Perform client side prediction of weapon effects.
cl_ragdoll_collide 0
cl_ragdoll_force_fade_time  0
cl_ragdoll_force_fade_time_local_view_player  0
cl_ragdoll_force_fade_time_on_moving_geo  0
cl_ragdoll_maxcount  0
cl_ragdoll_self_collision  0
cl_show_splashes  0
cl_showfiredbullets  1
cl_showfps 1
cl_showpos 1
cl_simdbones_slerp  1
cl_smooth  0
cl_threaded_bone_setup  1
cl_use_simd_bones  1
closecaption  1
csm_cascade_res  0
csm_coverage  0
csm_enabled  0
csm_quality_level  1
csm_renderable_shadows  0
csm_rope_shadows  0
csm_world_shadows  0
damage_indicator_style_pilot  1
disp_dynamic  0 //Do not use dynamic meshses for world geometry
dlight_enable  0
dodge_viewTiltMax  0
dof_enable  0
dof_overrideParams  0
dvs_enable  0 //Enable dynamic viewport scaling.
engine_no_focus_sleep  1 //Limit FPS when the engine is not focused
env_lightglow  0
exec usersettings.cfg
flex_rules  0
flex_smooth  0
fog_enable  0
fog_enable_water_fog  0
fog_enableskybox  0
fog_volume  0
fps_max 300
func_break_max_pieces  0
g_ragdoll_fadespeed "10000"//The rate of ragdoll fading
g_ragdoll_lvfadespeed "10000"//The rate of ragdoll fading in low violence
host_sleep  0
host_threaded_sound  0
hud_setting_adsDof  0
hud_setting_anonymousMode  1
hud_setting_damageTextStyle 3
hud_setting_minimapRotate  1    // This setting allows the minimap to rotate with you (default 0)
hud_setting_pingAlpha "0.4"     // Opacity of the pings and downed banners (default 1)
hud_setting_pingDoubleTapEnemy  1
hud_setting_streamerMode  1
hudchat_new_message_fade_duration  1
lightmap_ambient  0
lightmap_realtimelight  0
lightmap_realtimeshadows  0
m_acceleration  0
m_filter  0                     // Makes sure any kind of mouse filtering is off
m_rawinput  1                   // Takes the direct input of your mouse
map_settings_override  1
mat_antialias  0
mat_antialias_mode  0
mat_autoexposure_override_min_max  1
mat_backbuffer_count  0
mat_bloom_max_lighting_value  0
mat_bloom_scalefactor_scalar 0  // Disables bloom (nothing to do with recoil, just the graphical effect you fn weirdo)
mat_bloom_streak_amount  0
mat_bloom_wide_amount  0
mat_bloomscale  0
mat_bumpmap  0
mat_colcorrection_disableentities  1
mat_colorcorrection  0
mat_colorcorrection_editor  0
mat_compressedtextures 1
mat_debug_tonemapping_disable  1
mat_depthbias_shadowmap  0
mat_depthbias_tightshadowmap  0
mat_depthfeather_enable  0
mat_depthtest_force_disabled  1
mat_diffuse  1
mat_disable_bloom  1
mat_disable_lightmap_ambient  1
mat_disable_lightmaps  1
mat_disable_lightwarp  1
mat_disable_model_ambient  1
mat_dof_enabled  0
mat_dynamic_tonemapping  0
mat_enable_ssr  0
mat_envmap_scale  1
mat_envmapsize  0
mat_envmaptgasize  0
mat_fastspecular  1
mat_filterlightmaps  0
mat_force_bloom  0
mat_fullbright 1                //Brighter materials/textures, very good to use.
mat_fxaa_enable  0
mat_global_lighting  0
mat_hdr_enabled  0
mat_hdr_level  0
mat_hide_sun_in_last_cascade  1
mat_instancing  1
mat_light_edit  1
mat_local_contrast_scale_override  0
mat_maxframelatency  0
mat_mip_linear  0
mat_motion_blur_enabled  0
mat_motion_blur_falling_intensity  0
mat_motion_blur_falling_max  0
mat_motion_blur_falling_min  0
mat_motion_blur_forward_enabled  0
mat_motion_blur_percent_of_screen_max  0
mat_motion_blur_rotation_intensity  0
mat_motion_blur_strength  0
mat_parallaxmap  0
mat_picmip 4
mat_queue_mode 2
mat_reducefillrate  1
mat_reduceparticles  1
mat_screen_blur_enabled 0
mat_screen_blur_override  1
mat_shadercount  0 //Forces the game into using multiple threads
mat_shadowstate  0
mat_specular  0
mat_sun_highlight_size  0
mat_use_compressed_hdr_textures  1
mat_vignette_enable  0
mat_vsync  0 //Ensure VSync is disabled by default
mat_vsync_mode  0
model_fadeRangeFraction  0
modeldecals_forceAllowed  0
monitor_mat_sharpen_amount  0
mp_decals  0 //Disable decals
mp_usehwmmodels -1 //Do not use or load high quality characters
mp_usehwmvcds   -1 //Do not use or load high quality character facial expressions
muzzleflash_light  0
nb_shadow_dist  0
noise_filter_scale 0            // Removes Film-grain
particle_cpu_level  0
particle_dlights_enable  0
particle_gpu_level  0
pertrianglecollision  0
pin_opt_in 0
player_setting_damage_closes_deathbox_menu  0           // Your inventory wont auto-close anymore when receiving damage
projectile_faketrails  0
projectile_filltrails  2                                //Fill the gap between the gun barrel and the first seen projectile position for trail
prop_active_gib_limit  0
pvs_yield  1
r_DrawBeams  0
r_DrawDisp  0
r_PhysPropLighting  0
r_WaterDrawReflection  0
r_blurmenubg  0
r_createmodeldecals  0
r_decals  0
r_ditherAlpha  0
r_ditherFade  0
r_drawbatchdecals  0
r_drawbrushmodels  0
r_drawentities  0
r_drawopaquerenderables  0
r_drawparticles  0
r_drawscreenspaceparticles  0
r_drawsky  0
r_drawsprites  0
r_drawstaticlight  0
r_drawstaticprops  0
r_drawtranslucentrenderables  0
r_drawworld  0
r_dxgi_max_frame_latency 0
r_dynamic 0
r_dynamiclighting  0
r_forcecheapwater  1
r_fullscreen 1
r_jiggle_bones  0
r_lightmap  0
r_lightstyle  0
r_modeldecal_maxtotal  0
r_norefresh  1 //Do not store a useless and unused frame time variable
r_particle_lighting_enable  0
r_particle_lighting_force  0
r_particle_low_res_enable  1
r_particle_sim_spike_threshold_ms  0
r_particle_timescale 3
r_particles_cull_all  0
r_queued_ropes  1
r_rimlight  0
r_rootlod 2
r_ropetranslucent  0 //Skip simulating ropes
r_shadowrendertotexture  0
r_sse_s  0
r_threaded_particles  1
r_threadeddetailprops  1
r_txaaEnabled  0
r_updaterefracttexture  0
r_updaterefracttexture_allowmultiple  0
r_visambient  0
r_vismodellighting  0
r_visualizetraces  0
r_volumetric_lighting_enabled  0
r_waterdrawreflection  0
r_waterdrawrefraction  0
r_waterforceexpensive  0
r_waterforcereflectentities  0
ragdoll_sleepaftertime  0
rope_averagelight  0  //(1)Only use average light, instead of an extra max intensity average with 0. (0) Simplify rope lighting for weak GPUs, at the cost of a bit of CPU time
rope_collide  0 //Skip CPU heavy world collisions for ropes
rope_rendersolid  0  //Skip rendering solid part of ropes
rope_smooth  0 //Skip a long smoothing operation for ropes
rope_solid_minalpha  0 //Skip drawing non-solid part of ropes
rope_solid_minwidth "0.1"//Skip drawing ropes if they are not large enough on screen
rope_subdiv  0 //Skip heavy loops for rope subdivisions
rope_wind_dist  0 //Do not apply CPU intensive wind to ropes
rui_overrideVguiTextRendering  1
shadow_capable  0
shadow_default_filter_size  0
shadow_depth_dimen_min  0
shadow_depth_upres_factor_max  0
shadow_enable  0
shadow_filter_maxstep  0
shadow_maxdynamic  0
shadow_maxspotshadows  0
shadow_multisampled  0
shake_offsetFactor_human  0
showfps_enabled  1
showfps_heightpercent  0
showfps_mouse_latency  1
showfps_smoothtime  0
showfps_spinner  0
showhitlocation  1
showmem_enabled  0
shownet_enabled  0
showsnapshot_enabled  0
sleep_when_meeting_framerate  0
sleep_when_meeting_framerate_headroom_ms  0
sort_opaque_meshes  0
sprint_view_shake_style 1       // Less Headbob
ssao_blur 0
ssao_downsample  0
ssao_enabled 0
ssao_radius 59
sssss_enable  0
static_shadow  0
static_shadow_res  0
stream_cache_high_priority_static_models  1
stream_cache_preload_from_rpak  1
stream_drop_unused  1
stream_enable  0
stream_mips_use_staging_texture  0
stream_picmip 4
telemetry_client_enable 0
telemetry_client_sendInterval 0
tf_particles_disable_weather  1
toggle_on_jump_to_deactivate 0
toggle_on_jump_to_deactivate_changed 0
tracer_extra  0
tsaa_blendfactoroverride  1
tsaa_curframeblendamount "0.05"
tsaa_numsamples 64
tweak_light_shadows_every_frame  0
twitch_prime_linked 1
viewmodelShake  0
viewmodelShake_sourceRollRange  0
viewmodel_selfshadow  0
violence_ablood  0
violence_agibs  0
violence_hblood  0
violence_hgibs  0
vphysics_threadmode  1
vsm_ignore_face_planes  1
r_fastzreject  {-1 if nv_gpu else 0}
{"r_shadows 0" if shadow_ok else ""}
''')
