from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from interface_tester.schema_base import DataBagSchema


class NginxRouteRequirerSchema(BaseModel):
    service_hostname: str = Field(
        alias="service-hostname",
        description="The hostname of the service to create an ingress for.",
        examples=["example.com"],
        title="Service Hostname",
    )
    service_name: str = Field(
        alias="service-name",
        description="The name of the service to create an ingress for.",
        examples=["wordpress", "indico"],
        title="Service Name",
    )
    service_namespace: str = Field(
        alias="service-namespace",
        description="The namespace of the service to create an ingress for. Will default to the namespace this charm is deployed into.",
        examples=[],
        title="Service Namespace",
    )
    service_port: int = Field(
        alias="service-port",
        description="The port of the service to create an ingress for.",
        examples=[8080, 80],
        title="Service Port",
    )
    additional_hostnames: Optional[str] = Field(
        None,
        alias="additional-hostnames",
        description="Comma-separated list of additional hostnames for this ingress to listen on.",
        examples=["www.example.com,example.com"],
        title="Additional Hostnames",
    )
    ingress_class: Optional[str] = Field(
        None,
        alias="ingress-class",
        description='The ingress class to target for this ingress resource. If your cluster has multiple ingress controllers, this allows you to select the correct one, by setting the ingressClassName field on the ingress resource created by the charm. This value isn\'t available to be set via the relation as it\'s a property of the cluster\'s configuration. If this value is empty, the charm will use whichever ingress class has the "ingressclass.kubernetes.io/is-default-class" annotation set to "true". If multiple ingress classes are so configured, no selection will be made. For more details, see:  * https://kubernetes.github.io/ingress-nginx/user-guide/multiple-ingress/  * https://kubernetes.io/docs/concepts/services-networking/ingress/#default-ingress-class ',
        examples=["nginx"],
        title="Ingress Class",
    )
    limit_rps: Optional[int] = Field(
        None,
        alias="limit-rps",
        description="Number of requests accepted from a given IP each second. The burst limit is set to this limit multiplied by 5. When clients exceed this limit a 503 error will be returned. Setting this to 0 disables rate-limiting. ",
        examples=[],
        title="Limit Rps",
    )
    limit_whitelist: Optional[str] = Field(
        None,
        alias="limit-whitelist",
        description="If rate-limiting is set, client IP source ranges to be excluded. The value is a comma-separated list of CIDRs. ",
        examples=["10.0.0.0/8,172.16.0.0/12,192.168.0.0/16"],
        title="Limit Whitelist",
    )
    max_body_size: Optional[int] = Field(
        None,
        alias="max-body-size",
        description="Max allowed body-size (for file uploads) in megabytes, set to 0 to disable limits.",
        examples=[],
        title="Max Body Size",
    )
    owasp_modsecurity_crs: Optional[bool] = Field(
        None,
        alias="owasp-modsecurity-crs",
        description="Enable OWASP ModSecurity Core Rule Set (CRS). A set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts. See https://github.com/coreruleset/coreruleset for more details. ",
        examples=[],
        title="Owasp Modsecurity Crs",
    )
    owasp_modsecurity_custom_rules: Optional[str] = Field(
        None,
        alias="owasp-modsecurity-custom-rules",
        description="New line ('\\n') separated list of custom rules to be added to modsecurity-snippet annotation.",
        examples=[
            "SecAction id:900130,phase:1,nolog,pass,t:none,setvar:tx.crs_exclusions_wordpress=1\n"
        ],
        title="Owasp Modsecurity Custom Rules",
    )
    path_routes: Optional[str] = Field(
        None,
        alias="path-routes",
        description='Comma separated list of the routes under the hostname that you wish to map to the relation. Example: "/admin,/portal" will map example.test/admin and example.test/portal only. ',
        examples=["/admin,/portal", "/something(/|$)(.*)"],
        title="Path Routes",
    )
    proxy_read_timeout: Optional[int] = Field(
        None,
        alias="proxy-read-timeout",
        description="Defines a timeout in seconds for reading a response from the proxied server.",
        examples=[],
        title="Proxy Read Timeout",
    )
    retry_errors: Optional[str] = Field(
        None,
        alias="retry-errors",
        description='Specifies in which cases a request should be retried against the next server. Comma-separated list, e.g. "error,timeout,http_502,http_503,http_504". See http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_next_upstream for more details. Unrecognised values will be ignored. The nginx default will be used if this config option is set to an empty value. ',
        examples=["error,timeout,http_502,http_503,http_504"],
        title="Retry Errors",
    )
    rewrite_enabled: Optional[bool] = Field(
        None,
        alias="rewrite-enabled",
        description="Whether requests should be written to the `rewrite-target`",
        examples=[],
        title="Rewrite Enabled",
    )
    rewrite_target: Optional[str] = Field(
        None,
        alias="rewrite-target",
        description='The path to rewrite requests to. If not set, rewrite-target will be "/".',
        examples=["/app1", "/$2"],
        title="Rewrite Target",
    )
    session_cookie_max_age: Optional[int] = Field(
        None,
        alias="session-cookie-max-age",
        description="The max age to configure a session cookie for. Leaving unset or setting to 0 will disable session cookies and cookie-based affinity.",
        examples=[],
        title="Session Cookie Max Age",
    )
    tls_secret_name: Optional[str] = Field(
        None,
        alias="tls-secret-name",
        description="The name of the TLS secret to use. Leaving this empty will configure an ingress with TLS disabled.",
        examples=[],
        title="Tls Secret Name",
    )
    whitelist_source_range: Optional[str] = Field(
        None,
        alias="whitelist-source-range",
        description="Allowed client IP source ranges. The value is a comma separated list of CIDRs.",
        examples=["10.0.0.0/8,172.16.0.0/12,192.168.0.0/16"],
        title="Whitelist Source Range",
    )


class ProviderSchema(DataBagSchema):
    """Provider schema for nginx_route."""


class RequirerSchema(DataBagSchema):
    """Requirer schema for nginx_route."""

    app: NginxRouteRequirerSchema
