aux_source_directory(src Path_M2)

add_library(M1 STATIC ${Path_M2})

target_include_directories(M2 PUBLIC include)
target_link_libraries(M2 PUBLIC A1 A2)