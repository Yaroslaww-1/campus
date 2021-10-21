using System;
using System.Collections.Generic;

namespace GatewayApi.Options
{
    public class ServicesOptions
    {
        public const string Position = "Services";

        public Dictionary<string, string> Hosts { get; set; }
    }
}
