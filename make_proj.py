import argparse
import uuid
import os
import importlib

from Cheetah.Template import Template

parser = argparse.ArgumentParser()
parser.add_argument("--out_dir", help='Output directory', action='store')
parser.add_argument(
    "--proj_dir",
    help='Project file directory', action='store', default='.')
parser.add_argument('--pch', action='store_true')
parser.add_argument('--x86', action='store_true')
parser.add_argument('--x64', action='store_true')
parser.add_argument(
    '--msvc', help='MSVC version to generate for', default='vs2015')
parser.add_argument(
    '--num', help='Number of entry points', type=int, default=1)
parser.add_argument(
    '--alpha', help='Use letters for multiple files', action='store_true')
parser.add_argument("name")
args = parser.parse_args()

if not args.x86 and not args.x64:
    print 'Must specify at least one architecture'
    exit(1)

template_dir = 'templates' + '.' + args.msvc
templates = [
    'filter_template', 'vcxproj_template', 'console_cpp_template',
    'precompiled_hpp_template', 'precompiled_cpp_template'
]

for t in templates:
    importlib.import_module('templates' + '.' + template_dir + '.', t)
# from templates_dir import (
#     filter_template, vcxproj_template, console_cpp_template,
#     precompiled_hpp_template, precompiled_cpp_template
# )

uuid.variant = uuid.RESERVED_MICROSOFT
proj_name = args.name
out_dir = args.out_dir or proj_name
proj_dir = args.proj_dir

# compute relative path from project directory to cpp files
rel_path = os.path.relpath(out_dir, os.path.join(out_dir, proj_dir))
if rel_path == '.':
    rel_path = ''
else:
    rel_path = rel_path + os.sep

cfg = {
    'proj_guid': uuid.uuid4(),
    'src_guid': uuid.uuid4(),
    'inc_guid': uuid.uuid4(),
    'proj_name': proj_name,
    'rel_path': rel_path,
    'with_pch': args.pch,
    'with_x86': args.x86,
    'with_x64': args.x64,
}

for d in [out_dir, os.path.join(out_dir, proj_dir)]:
    if not os.path.exists(d):
        os.makedirs(d)


def template_to_file(template, filename):
    t = Template(template, cfg)
    with open(os.path.join(out_dir, filename), 'wt') as f:
        f.write(str(t))


def prj_to_file(template, filename):
    t = Template(template, cfg)
    with open(os.path.join(out_dir, proj_dir, filename), 'wt') as f:
        f.write(str(t))

prj_to_file(filter_template, proj_name + '.vcxproj.filter')
prj_to_file(vcxproj_template, proj_name + '.vcxproj')
template_to_file(console_cpp_template, proj_name + '.cpp')
if args.pch:
    template_to_file(precompiled_hpp_template, 'precompiled.hpp')
    template_to_file(precompiled_cpp_template, 'precompiled.cpp')
