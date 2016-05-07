filter_template = r"""<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup>
    <Filter Include="src">
      <UniqueIdentifier>{${src_guid}}</UniqueIdentifier>
      <Extensions>cpp;c;cc;cxx;def;odl;idl;hpj;bat;asm;asmx</Extensions>
    </Filter>
    <Filter Include="inc">
      <UniqueIdentifier>{${inc_guid}}</UniqueIdentifier>
      <Extensions>h;hh;hpp;hxx;hm;inl;inc;xsd</Extensions>
    </Filter>
  </ItemGroup>
#if $with_pch
  <ItemGroup>
    <ClInclude Include="precompiled.hpp">
      <Filter>inc</Filter>
    </ClInclude>
  </ItemGroup>
#end if
  <ItemGroup>
    <ClCompile Include="${proj_name}.cpp">
      <Filter>src</Filter>
    </ClCompile>
#if $with_pch
    <ClCompile Include="precompiled.cpp">
      <Filter>src</Filter>
    </ClCompile>
#end if
  </ItemGroup>
</Project>
"""
