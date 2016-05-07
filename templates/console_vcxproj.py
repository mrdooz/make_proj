vcxproj_template = r"""<?xml version="1.0" encoding="utf-8"?>
<Project DefaultTargets="Build" ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup Label="ProjectConfigurations">
#if $with_x86
    <ProjectConfiguration Include="Debug|Win32">
      <Configuration>Debug</Configuration>
      <Platform>Win32</Platform>
    </ProjectConfiguration>
    <ProjectConfiguration Include="Release|Win32">
      <Configuration>Release</Configuration>
      <Platform>Win32</Platform>
    </ProjectConfiguration>
#end if
#if $with_x64
    <ProjectConfiguration Include="Debug|x64">
      <Configuration>Debug</Configuration>
      <Platform>x64</Platform>
    </ProjectConfiguration>
    <ProjectConfiguration Include="Release|x64">
      <Configuration>Release</Configuration>
      <Platform>x64</Platform>
    </ProjectConfiguration>
#end if
  </ItemGroup>
  <PropertyGroup Label="Globals">
    <ProjectGuid>{${proj_guid}}</ProjectGuid>
    <Keyword>Win32Proj</Keyword>
    <RootNamespace>${proj_name}</RootNamespace>
    <WindowsTargetPlatformVersion>8.1</WindowsTargetPlatformVersion>
  </PropertyGroup>
  <Import Project="\$(VCTargetsPath)\Microsoft.Cpp.Default.props" />
#if $with_x86
  <PropertyGroup Condition="'\$(Configuration)|\$(Platform)'=='Debug|Win32'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>true</UseDebugLibraries>
    <PlatformToolset>v140_xp</PlatformToolset>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <PropertyGroup Condition="'\$(Configuration)|\$(Platform)'=='Release|Win32'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>false</UseDebugLibraries>
    <PlatformToolset>v140_xp</PlatformToolset>
    <WholeProgramOptimization>true</WholeProgramOptimization>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
#end if
#if $with_x64
  <PropertyGroup Condition="'\$(Configuration)|\$(Platform)'=='Debug|x64'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>true</UseDebugLibraries>
    <PlatformToolset>v140</PlatformToolset>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <PropertyGroup Condition="'\$(Configuration)|\$(Platform)'=='Release|x64'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>false</UseDebugLibraries>
    <PlatformToolset>v140</PlatformToolset>
    <WholeProgramOptimization>true</WholeProgramOptimization>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
#end if
  <Import Project="\$(VCTargetsPath)\Microsoft.Cpp.props" />
  <ImportGroup Label="ExtensionSettings">
  </ImportGroup>
  <ImportGroup Label="Shared">
  </ImportGroup>
#if $with_x86
  <ImportGroup Label="PropertySheets" Condition="'\$(Configuration)|\$(Platform)'=='Debug|Win32'">
    <Import Project="\$(UserRootDir)\Microsoft.Cpp.\$(Platform).user.props" Condition="exists('\$(UserRootDir)\Microsoft.Cpp.\$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'\$(Configuration)|\$(Platform)'=='Release|Win32'">
    <Import Project="\$(UserRootDir)\Microsoft.Cpp.\$(Platform).user.props" Condition="exists('\$(UserRootDir)\Microsoft.Cpp.\$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
#end if
#if $with_x64
  <ImportGroup Label="PropertySheets" Condition="'\$(Configuration)|\$(Platform)'=='Debug|x64'">
    <Import Project="\$(UserRootDir)\Microsoft.Cpp.\$(Platform).user.props" Condition="exists('\$(UserRootDir)\Microsoft.Cpp.\$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'\$(Configuration)|\$(Platform)'=='Release|x64'">
    <Import Project="\$(UserRootDir)\Microsoft.Cpp.\$(Platform).user.props" Condition="exists('\$(UserRootDir)\Microsoft.Cpp.\$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
#end if
  <PropertyGroup Label="UserMacros" />
#if $with_x86
  <PropertyGroup Condition="'\$(Configuration)|\$(Platform)'=='Debug|Win32'">
    <LinkIncremental>true</LinkIncremental>
  </PropertyGroup>
#end if
#if $with_x64
  <PropertyGroup Condition="'\$(Configuration)|\$(Platform)'=='Debug|x64'">
    <LinkIncremental>true</LinkIncremental>
  </PropertyGroup>
#end if
#if $with_x86
  <PropertyGroup Condition="'\$(Configuration)|\$(Platform)'=='Release|Win32'">
    <LinkIncremental>false</LinkIncremental>
  </PropertyGroup>
#end if
#if $with_x64
  <PropertyGroup Condition="'\$(Configuration)|\$(Platform)'=='Release|x64'">
    <LinkIncremental>false</LinkIncremental>
  </PropertyGroup>
#end if
#if $with_x86
  <ItemDefinitionGroup Condition="'\$(Configuration)|\$(Platform)'=='Debug|Win32'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <Optimization>Disabled</Optimization>
      <PreprocessorDefinitions>WIN32;_DEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
#if $with_pch
      <PrecompiledHeader>Use</PrecompiledHeader>
      <PrecompiledHeaderFile>precompiled.hpp</PrecompiledHeaderFile>
      <ForcedIncludeFiles>precompiled.hpp</ForcedIncludeFiles>
#end if      
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
#end if
#if $with_x64
  <ItemDefinitionGroup Condition="'\$(Configuration)|\$(Platform)'=='Debug|x64'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <Optimization>Disabled</Optimization>
      <PreprocessorDefinitions>_DEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
#if $with_pch
      <PrecompiledHeader>Use</PrecompiledHeader>
      <PrecompiledHeaderFile>precompiled.hpp</PrecompiledHeaderFile>
      <ForcedIncludeFiles>precompiled.hpp</ForcedIncludeFiles>
#end if      
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
#end if
#if $with_x86
  <ItemDefinitionGroup Condition="'\$(Configuration)|\$(Platform)'=='Release|Win32'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <Optimization>MaxSpeed</Optimization>
      <FunctionLevelLinking>true</FunctionLevelLinking>
      <IntrinsicFunctions>true</IntrinsicFunctions>
      <PreprocessorDefinitions>WIN32;NDEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
#if $with_pch
      <PrecompiledHeader>Use</PrecompiledHeader>
      <PrecompiledHeaderFile>precompiled.hpp</PrecompiledHeaderFile>
      <ForcedIncludeFiles>precompiled.hpp</ForcedIncludeFiles>
#end if      
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <EnableCOMDATFolding>true</EnableCOMDATFolding>
      <OptimizeReferences>true</OptimizeReferences>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
#end if
#if $with_x64
  <ItemDefinitionGroup Condition="'\$(Configuration)|\$(Platform)'=='Release|x64'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <Optimization>MaxSpeed</Optimization>
      <FunctionLevelLinking>true</FunctionLevelLinking>
      <IntrinsicFunctions>true</IntrinsicFunctions>
      <PreprocessorDefinitions>NDEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
#if $with_pch
      <PrecompiledHeader>Use</PrecompiledHeader>
      <PrecompiledHeaderFile>precompiled.hpp</PrecompiledHeaderFile>
      <ForcedIncludeFiles>precompiled.hpp</ForcedIncludeFiles>
#end if
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <EnableCOMDATFolding>true</EnableCOMDATFolding>
      <OptimizeReferences>true</OptimizeReferences>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
#end if
#if $with_pch
  <ItemGroup>
    <ClInclude Include="${rel_path}precompiled.hpp" />
  </ItemGroup>
  <ItemGroup>
    <ClCompile Include="${rel_path}${proj_name}.cpp">
      <PrecompiledHeaderFile Condition="'\$(Configuration)|\$(Platform)'=='Debug|Win32'">precompiled.hpp</PrecompiledHeaderFile>
      <PrecompiledHeaderFile Condition="'\$(Configuration)|\$(Platform)'=='Release|Win32'">precompiled.hpp</PrecompiledHeaderFile>
      <PrecompiledHeaderFile Condition="'\$(Configuration)|\$(Platform)'=='Debug|x64'">precompiled.hpp</PrecompiledHeaderFile>
      <PrecompiledHeaderFile Condition="'\$(Configuration)|\$(Platform)'=='Release|x64'">precompiled.hpp</PrecompiledHeaderFile>
    </ClCompile>
    <ClCompile Include="${rel_path}precompiled.cpp">
      <PrecompiledHeader Condition="'\$(Configuration)|\$(Platform)'=='Debug|Win32'">Create</PrecompiledHeader>
      <PrecompiledHeader Condition="'\$(Configuration)|\$(Platform)'=='Debug|x64'">Create</PrecompiledHeader>
      <PrecompiledHeader Condition="'\$(Configuration)|\$(Platform)'=='Release|Win32'">Create</PrecompiledHeader>
      <PrecompiledHeader Condition="'\$(Configuration)|\$(Platform)'=='Release|x64'">Create</PrecompiledHeader>
    </ClCompile>
  </ItemGroup>
#else
  <ItemGroup>
    <ClCompile Include="${rel_path}${proj_name}.cpp">
    </ClCompile>
  </ItemGroup>
#end if
  <Import Project="\$(VCTargetsPath)\Microsoft.Cpp.targets" />
  <ImportGroup Label="ExtensionTargets">
  </ImportGroup>
</Project>
"""
