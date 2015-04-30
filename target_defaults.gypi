#

{
    'conditions': [
        ['">(toolset)"=="clang"', {
          'make_global_settings': [
            ['CC', '/usr/bin/clang'],
            ['CXX', '/usr/bin/clang++'],
          ],
        }],
      ],

	'target_defaults': {
        # include for all projects
        'include_dirs': [
            '<(EXT_BOOST)/include',
        ],
        'target_conditions': [
            ['_type=="executable" and OS!="win"', {
                'cflags': ['-fPIC'],
                'library_dirs': [
                    '<(EXT_BOOST)/lib',
                ],
            }],
            ['_type=="static_library" and OS!="win"', {
                'standalone_static_library': 1, # for ar using alink (ar crs) rather than alink_thin
            }],
            ['_type=="shared_library" and OS!="win"', {
                'cflags': ['-fPIC'],
                'library_dirs': [
                    '<(EXT_BOOST)/lib',
                ],
            }],
            ['OS!="win"', {
                'sources/': [
                  ['exclude', '_win'],
                ],
            }],
            ['OS!="linux"', {
                'sources/': [
                  ['exclude', '_linux'],
                ],
            }],
        ],
        'conditions': [
            ['OS=="linux"', {
                'cflags': [
                    '-fpermissive',
                    '-std=c++11',
                ],
                }, { # win
                'configurations': {
                    'Common': {
                         'abstract': 1,
                         'msvs_disabled_warnings': [4819,],
                         'msvs_configuration_attributes': {
                            'OutputDirectory': 'out/<(VCVER)/$(ProjectName)/$(Configuration)/$(Platform)',
                            'IntermediateDirectory': 'out/<(VCVER)/$(ProjectName)/$(Configuration)/$(Platform)',
                         },
                         'msvs_settings': {
                            'VCCLCompilerTool': {
                                'Optimization': '0',
                                'WarningLevel': '3',
                                'WarnAsError': 'false',
                                'BufferSecurityCheck': 'false',
                                'MinimalRebuild': 'true',
                                'ProgramDataBaseFileName': '$(OutDir)/$(ProjectName).pdb',
                                'PreprocessorDefinitions' : [
                                    '_CRT_SECURE_NO_WARNINGS',
                                    '_WIN32_WINNT=0x0501',
                                ],
                            },
                            'target_conditions': [
                                ['_type=="executable"', {
                                    'VCLinkerTool': {
                                    'GenerateDebugInformation': 'true',
                                    'LinkIncremental': '2',
                                    'ProgramDatabaseFile': '$(OutDir)/$(ProjectName).pdb',
                                    'SubSystem': '1',
                                    'RandomizedBaseAddress': '1',
                                    'DataExecutionPrevention': '0',
                                },
                                },],
                                ['_type=="shared_library"', {
                                    'VCLinkerTool': {
                                    'GenerateDebugInformation': 'true',
                                    'LinkIncremental': '2',
                                    'ProgramDatabaseFile': '$(OutDir)/$(ProjectName).pdb',
                                    'SubSystem': '1',
                                    'RandomizedBaseAddress': '1',
                                    'DataExecutionPrevention': '0',
                                },
                                },],
                            ],
                        },
                    },
                    'Debug_Dynamic_Win32': {
                        'inherit_from': ['Common'],
                        'msvs_configuration_platform': 'Win32',
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'PreprocessorDefinitions' : [
                                    '_DEBUG',
                                ],
                                'RuntimeLibrary' : '3',
                                'DebugInformationFormat': '4',
                            },
                        },
                    },
                    'Release_Dynamic_Win32': {
                        'inherit_from': ['Common'],
                        'msvs_configuration_platform': 'Win32',
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'PreprocessorDefinitions' : [
                                    'NDEBUG',
                                ],
                                'RuntimeLibrary' : '2',
                                'DebugInformationFormat': '4',
                            },
                        },
                    },
                    'Debug_Static_Win32': {
                        'inherit_from': ['Common'],
                        'msvs_configuration_platform': 'Win32',
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'PreprocessorDefinitions' : [
                                    '_DEBUG',
                                ],
                                'RuntimeLibrary' : '1',
                                'DebugInformationFormat': '4',
                            },
                        },
                    },
                    'Release_Static_Win32': {
                        'inherit_from': ['Common'],
                        'msvs_configuration_platform': 'Win32',
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'PreprocessorDefinitions' : [
                                    'NDEBUG',
                                ],
                                'RuntimeLibrary' : '0',
                                'DebugInformationFormat': '4',
                            },
                        },
                    },
                    'Debug_Dynamic_x64': {
                        'inherit_from': ['Common'],
                        'msvs_configuration_platform': 'x64',
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'PreprocessorDefinitions' : [
                                    '_DEBUG',
                                ],
                                'RuntimeLibrary' : '3',
                                'DebugInformationFormat': '3',
                            },
                        },
                    },
                    'Release_Dynamic_x64': {
                        'inherit_from': ['Common'],
                        'msvs_configuration_platform': 'x64',
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'PreprocessorDefinitions' : [
                                    'NDEBUG',
                                ],
                                'RuntimeLibrary' : '2',
                                'DebugInformationFormat': '3',
                            },
                        },
                    },
                    'Debug_Static_x64': {
                        'inherit_from': ['Common'],
                        'msvs_configuration_platform': 'x64',
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'PreprocessorDefinitions' : [
                                    '_DEBUG',
                                ],
                                'RuntimeLibrary' : '1',
                                'DebugInformationFormat': '3',
                            },
                        },
                    },
                    'Release_Static_x64': {
                        'inherit_from': ['Common'],
                        'msvs_configuration_platform': 'x64',
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'PreprocessorDefinitions' : [
                                    'NDEBUG',
                                ],
                                'RuntimeLibrary' : '0',
                                'DebugInformationFormat': '3',
                            },
                        },
                    },
                    # common configuration for test projects
                    'Debug_Dynamic_Win32_Test': {
                        'abstract': 1,
                        'msvs_settings': {
                            'VCLinkerTool': {
                                'AdditionalLibraryDirectories': [
                                    '<(EXT_CPPUNIT)/lib/<(VCVER)',
                                ],
                                'AdditionalDependencies': [
                                    'cppunitd.lib',
                                ],
                            },
                        },
                    },
                    'Release_Dynamic_Win32_Test': {
                        'abstract': 1,
                        'msvs_settings': {
                            'VCLinkerTool': {
                                'AdditionalLibraryDirectories': [
                                    '<(EXT_CPPUNIT)/lib/<(VCVER)',
                                    '<(EXT_BOOST)/lib',
                                ],
                                'AdditionalDependencies': [
                                    'cppunit.lib',
                                ],
                            },
                        },
                    },
                    'Debug_Static_Win32_Test': {
                        'abstract': 1,
                        'msvs_settings': {
                            'VCLinkerTool': {
                                'AdditionalLibraryDirectories': [
                                    '<(EXT_CPPUNIT)/lib/<(VCVER)',
                                    '<(EXT_BOOST)/lib',
                                ],
                                'AdditionalDependencies': [
                                    'cppunitsd.lib',
                                ],
                            },
                        },
                    },
                    'Release_Static_Win32_Test': {
                        'abstract': 1,
                        'msvs_settings': {
                            'VCLinkerTool': {
                                'AdditionalLibraryDirectories': [
                                    '<(EXT_CPPUNIT)/lib/<(VCVER)',
                                    '<(EXT_BOOST)/lib',
                                ],
                                'AdditionalDependencies': [
                                    'cppunits.lib',
                                ],
                            },
                        },
                    },
                    'Debug_Dynamic_x64_Test': {
                        'abstract': 1,
                        'msvs_settings': {
                            'VCLinkerTool': {
                                'AdditionalLibraryDirectories': [
                                    '<(EXT_CPPUNIT)/lib/<(VCVER)/x64',
                                    '<(EXT_BOOST)/lib/x64',
                                ],
                                'AdditionalDependencies': [
                                    'cppunitd.lib',
                                ],
                            },
                        },
                    },
                    'Release_Dynamic_x64_Test': {
                        'abstract': 1,
                        'msvs_settings': {
                            'VCLinkerTool': {
                                'AdditionalLibraryDirectories': [
                                    '<(EXT_CPPUNIT)/lib/<(VCVER)/x64',
                                    '<(EXT_BOOST)/lib/x64',
                                ],
                                'AdditionalDependencies': [
                                    'cppunit.lib',
                                ],
                            },
                        },
                    },
                    'Debug_Static_x64_Test': {
                        'abstract': 1,
                        'msvs_settings': {
                            'VCLinkerTool': {
                                'AdditionalLibraryDirectories': [
                                    '<(EXT_CPPUNIT)/lib/<(VCVER)/x64',
                                    '<(EXT_BOOST)/lib/x64',
                                ],
                                'AdditionalDependencies': [
                                    'cppunitsd.lib',
                                ],
                            },
                        },
                    },
                    'Release_Static_x64_Test': {
                        'abstract': 1,
                        'msvs_settings': {
                            'VCLinkerTool': {
                                'AdditionalLibraryDirectories': [
                                    '<(EXT_CPPUNIT)/lib/<(VCVER)/x64',
                                    '<(EXT_BOOST)/lib/x64',
                                ],
                                'AdditionalDependencies': [
                                    'cppunits.lib',
                                ],
                            },
                        },
                    },
                    # end of common configuration for test projects
                },
            },],
        ],
    },

}
